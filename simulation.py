import random


# """model = [{skill:45,luck:5,total:50}]"""


def make_participants(total_participants,skill_max_percentage=100,luck_percentage_max=5):
    participants_list = []
    for i in range(total_participants):
        skill = random.randint(0,skill_max_percentage)
        luck = random.randint(0,luck_percentage_max)
        participants_list.append({'skill':skill,'luck':luck,'total':skill+luck,'id':i})
    return participants_list

def luck(participants,top,total_participants):
    top_ten = []
    value = 0
    selected = 0
    selected_strip = 0
    for y in range(top):
        for i in range(total_participants-y):
            if participants[i]['total'] > value:
                value = participants[i]['total']
                selected = participants[i]
                selected_strip = i
        
        top_ten.append(selected)
        # print(selected)
        value=0
        participants.pop(selected_strip)
        # print(selected)
    return top_ten

def noluck(participants,top,total_participants):
    top_ten = []
    value = 0
    selected = 0
    selected_strip = 0
    for y in range(top):
        for i in range(total_participants-y):
            if participants[i]['skill'] > value:
                value = participants[i]['skill']
                selected = participants[i]
                selected_strip = i
        
        top_ten.append(selected)
        # print(selected)
        value=0
        participants.pop(selected_strip)
        # print(selected)
    return top_ten


def run(luck_percentage_max=5,total_participants=10,selects=10):
    skill_max_percentage = 100-luck_percentage_max

    participants_list = make_participants(total_participants,skill_max_percentage,luck_percentage_max)
    participants2 =participants_list.copy()
    with_luck = luck(participants_list,selects,total_participants)
    no_luck = noluck(participants2,selects,total_participants)

    same = 0
    for i in range(len(with_luck)):
        for j in range(len(no_luck)):
            if with_luck[i]['id'] == no_luck[j]['id']:
                same += 1
    return [with_luck,no_luck,same]


