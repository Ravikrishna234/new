"""Square root newton rapson"""
def main():
    """newton"""
    cons_tant = 0.01
    sq_in = int(input())
    sta_rt = sq_in/2.0
    while abs(sta_rt*sta_rt - sq_in) >= cons_tant:
        sta_rt = sta_rt - (((sta_rt**2) - sq_in)/(2*sta_rt))
    print(str(sta_rt))
if __name__ == "__main__":
    main()
