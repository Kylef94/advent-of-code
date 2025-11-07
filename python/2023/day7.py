from collections import Counter

def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            data.append(l.strip().split(' '))
    return data

handtypes = ['HIGH', 'ONEP', 'TWOP', 'THREE', 'FULLH', 'FOUR', 'FIVE',]
      

cardranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

class Hand:
    
    def __init__(self, cards, bid) -> None:
        self.cards = cards
        self.bid = int(bid)
        self.type = self.gethand()
        
        
    def gethand(self):
        cardcount = Counter(self.cards)
        counts = cardcount.most_common()
        
        top_card = counts[0][0]
        top_count = counts[0][1]
        
        if top_card == 'J':
            if top_count < 5:
                second_card = counts[1][0]

                del cardcount['J']
                cardcount[second_card] += top_count
            
        else:
            jcount = cardcount['J']
            if jcount:
                cardcount[top_card] = top_count + jcount
                del cardcount['J']
                
        
        counts = cardcount.most_common()
        most_common_count = counts[0][1]
        
        if most_common_count < 5:
            second_most_common_count = counts[1][1]

        match most_common_count:
            case 5:
                return "FIVE"
            
            case 4:
            
                return "FOUR"
            
            case 3:
                if second_most_common_count == 2:
                    return 'FULLH'
                else:
                    return 'THREE'
            
            case 2:
                if second_most_common_count == 2:
                    return 'TWOP'
                else:
                    return 'ONEP'

            case 1:
                return 'HIGH'

    def __eq__(self, other) -> bool:
        if self.type != other.type:
            return False
        
        else:
            selfhand = list(self.cards)
            otherhand = list(other.cards)
            
            for h in zip(selfhand, otherhand):
                if h[0] != h[1]:
                    return False
            return True
        
    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return handtypes.index(self.type) < handtypes.index(other.type)
        
        else:
            selfhand = list(self.cards)
            otherhand = list(other.cards)
            
            for h in zip(selfhand, otherhand):
                if h[0] != h[1]:
                    return cardranks.index(h[0]) < cardranks.index(h[1])
            return False
        
    def __str__(self) -> str:
        return f"HAND: cards = {self.cards}, type = {self.type}, bid = {self.bid}"
    
if __name__ == "__main__":
    data = get_input()
    hands = []
    for d in data:
        hand = Hand(d[0], d[1])
        #print(hand)
        hands.append(hand)
    hands.sort()
    
    print("sorted:")
    for h in hands:
        print(h)

    total = 0
    for i in range(len(hands)):
        total += (i + 1) * hands[i].bid
    
    print(total)