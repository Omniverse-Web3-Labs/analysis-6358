import decimal

# The precision is 1 minute
MTBF = decimal.Decimal(120.)

WAITINGTIME = decimal.Decimal(5.)
OPTIME = decimal.Decimal(3.)

SYNCNUM = decimal.Decimal(10.)
CHAINNUM = decimal.Decimal(30.)

YEARMINUTES = 365 * 24 * 60

def prob_double_spend_attack(mtbf = MTBF, waitingtime = WAITINGTIME, optime = OPTIME, syncnum = SYNCNUM, chainnum = CHAINNUM):

    if waitingtime < optime:
        raise Exception("the `waiting time` must longer than the `optime`")
    
    hp_one = decimal.Decimal(1.)

    lmd_working = hp_one / mtbf
    lmd_submit = hp_one / optime

    # interval = optime
    # count = waitingtime / interval
    # print(interval, count)

    # p_success_interval = math.exp(-lmd_working * interval) * (1. - math.exp(-lmd_submit * interval))
    # print("success in one interval: ", p_success_interval)

    # p_fail_single = math.pow((1. - p_success_interval), count)
    # print("submitting to one chain failed with the waiting time: ", p_fail_single)

    p_s_2 = lmd_submit / (lmd_working + lmd_submit) * (hp_one - decimal.Decimal.exp(-(lmd_submit + lmd_working) * waitingtime))
    print("successful synchronization on one chain with one synchronizer: ", p_s_2)

    ps2_s_many = hp_one - ((hp_one - p_s_2) ** syncnum)
    print("successful synchronization on one chain with many synchronizers: ", ps2_s_many)

    ps2_all = (ps2_s_many ** chainnum)
    print("successful synchronization on all chains with many synchronizers:", ps2_all)

    ps2_dsa = hp_one - ps2_all
    print("The probability of double-spend attack: ", ps2_dsa)

    malicious_times_per_year = YEARMINUTES * ps2_dsa
    print("The supposed network fail times: ", YEARMINUTES / mtbf)
    print("successful attack times: ", malicious_times_per_year)


prob_double_spend_attack()
