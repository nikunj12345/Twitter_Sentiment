import sys
def check_cmd(length):
    if length==3:
        if sys.argv[1]=='AFINN-111.txt':
            return True
        else:
            print("Pass sentiment_score filename as first argument")
            print("and tweets filename as second argument")  
    else:
        if length==1:
            print("Pass  sentiment_score and tweets filename in commandline arguments")
        else:
            if length==2:
                if sys.argv[1]!='AFINN-111.txt':
                        print("Pass sentiment_score filename as first argument")       
                else:
                    print("Pass tweets filename also alongwith sentiment_score file")
    return False
