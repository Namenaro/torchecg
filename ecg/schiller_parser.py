import os
import json
import pickle as pkl
from ecg.preprocess import fix_baseline

PATH = "C:\\!mywork\\datasets\\data_schiller\\"
FILENAME1 = "C:\\mywork\\torchecg\\data\\fixed_diverse_012parts.pkl"
LEADS_NAMES = ['i', 'ii', 'iii', 'avr', 'avl', 'avf', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6']
SIGNAL_LEN = 5000
FREQUENCY_OF_DATASET = 500



def info(partname):
    with open(partname, 'r') as f:
        data = json.load(f)
        print(partname + "has "+ str(len(data.keys())))

def all_leads_from_all(partsnames):
    all_signals = []
    for partname in partsnames:
        with open(partname, 'r') as f:
            data = json.load(f)
            for case_id in data.keys():
                leads = data[case_id]['Leads']
                for lead_name in LEADS_NAMES:
                    lead_signal = leads[lead_name]['Signal']
                    if (len(lead_signal)) != SIGNAL_LEN:
                        print("problem with " + str(case_id))
                        continue
                    all_signals.append(lead_signal)
    return all_signals


def save_diverse_1D_dataset():
    DATAPARTS = [PATH + "data_part_0.json",
                 PATH + "data_part_1.json",
                 PATH + "data_part_2.json"]

    data = all_leads_from_all(DATAPARTS)
    fixed_data = fix_baseline(data, FREQUENCY_OF_DATASET)
    outfile = open(FILENAME1, 'wb')
    pkl.dump(fixed_data, outfile)
    outfile.close()
    print("dataset saved, datalen " + str(len(data)))

def open_diverse_1D_dataset():
    dataset = []
    if os.path.exists(FILENAME1):  #
        infile = open(FILENAME1, 'rb')
        dataset = pkl.load(infile)
        infile.close()
    return dataset


if __name__ == "__main__":
    #save_diverse_1D_dataset()
    dataset = open_diverse_1D_dataset()
    print (len(dataset))
