import random
import sys

def cards():
    
    h_cards = ['K','Q','j','1','2','3','4','5','6','7','8','9','A'] 
    d_cards = ['K','Q','j','1','2','3','4','5','6','7','8','9','A'] 
    s_cards = ['K','Q','j','1','2','3','4','5','6','7','8','9','A'] 
    c_cards = ['K','Q','j','1','2','3','4','5','6','7','8','9','A'] 
    deck = h_cards+d_cards+s_cards+c_cards
    
    random.shuffle(deck)
    
    try:
        while True:
            i = int(input("Enter the place you want to cut the deck :"))
            players = int(input("Enter the number of Players :"))
            if(i>52 or (52-i)/players<0):
                continue
            else:
                break
    except ValueError:
        sys.exit("OOPs!! you entered a non interger value.")
        
    else:
        
        print("P1 : P2 : P3 ")
        card_set = round((52-i)/players)
        for _ in range(card_set):
            
            print(f"{deck[i]} : {deck[(i+1)]} : {deck[(i+2)]}")
            i=i+3
            
            
def main():
     
     cards()
     
main()
              