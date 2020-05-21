import BaselineWanderRemoval as bwr

def fix_baseline(all_signals, frequency_of_dataset):
    print("start fixing baseline in  " + str(len(all_signals)) + " ecg signals...")
    i = 0
    all_fixed_signals = []
    for signal in all_signals:
        fixed_signal = bwr.fix_baseline_wander(signal, frequency_of_dataset)
        all_fixed_signals.append(fixed_signal)
        print(i)
        i+=1
    print ("Done!")
    return all_fixed_signals