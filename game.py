from time import sleep, time
sleep(1)
total_time = 0

for i in range(5):
    start_time = time()
    print('Quick, the Enter key')
    input()
    reaction_time = time() - start_time
    total_time = total_time + reaction_time
    print('That was fast, you only took ',reaction_time,'seconds')


print('Total Reaction time: ',total_time)
print('Average Reaction time: ',total_time/(i+1))
