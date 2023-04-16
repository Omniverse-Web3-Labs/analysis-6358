import math

# The precision is 1 minute
MTBF = 120
WAITINGTIME = 5
RECOVERTIME = 2

SYNCNUM = 25
CHAINNUM = 100

YEARMINUTES = 365 * 24 * 60

def prob_double_spend_attack(mtbf = MTBF, waitingtime = WAITINGTIME, recovertime = RECOVERTIME, syncnum = SYNCNUM, chainnum = CHAINNUM):
    lmd = 1. / mtbf;

    p_fail_single = (1. - math.pow(math.exp(-lmd * recovertime), chainnum)) ** (waitingtime / recovertime)
    print(p_fail_single)
    
    # p_fail = math.pow(math.exp(-lmd * WAITINGTIME), 2) * math.pow(p_fail_single, SYNCNUM)
    p_fail = math.pow(p_fail_single, syncnum)
    print(p_fail)



    malicious_times_per_year = YEARMINUTES * p_fail
    print("The suspected network fail times: ", YEARMINUTES / mtbf)
    print("successful attack times: ", malicious_times_per_year)


prob_double_spend_attack()
