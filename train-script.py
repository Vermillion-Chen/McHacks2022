import pandas as pd
import numpy as np
import datetime
from datetime import date, time, timedelta

null = [datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
        datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
        datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
        datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0)]

best = []
traintimes = null
traintimes[0] = datetime.time(7,0,0)
traintimes[1] = datetime.time(7,10,0)
best_time = 99999
cur_time = 99999

for i in range(5, 11, 5):
    traintimes[2] = (datetime.time(7,15+i,0)) 
    for i in range(5, 11, 5):
        traintimes[3] = (datetime.time(7,20+i,0)) 
        for i in range(5, 11, 5):
            traintimes[4] = (datetime.time(7,25+i,0)) 
            for i in range(5, 11, 5):
                traintimes[5] = (datetime.time(7,30+i,0)) 
                for i in range(5, 11, 5):
                    traintimes[6] = (datetime.time(7,35+i,0)) 
                    for i in range(5, 11, 5):
                        traintimes[7] = (datetime.time(7,40+i,0)) 
                        for i in range(5, 10, 4):
                            traintimes[8] = (datetime.time(7,50+i,0)) 
                            for i in range(5, 11, 5):
                                traintimes[9] = (datetime.time(8,15+i,0)) 
                                for i in range(5, 11, 5):
                                    traintimes[10] = (datetime.time(8,35+i,0)) 
                                    for i in range(5, 10, 4):
                                        traintimes[11] = (datetime.time(8,50+i,0)) 
                                        for i in range(5, 11, 5):
                                            traintimes[12] = (datetime.time(9,15+i,0)) 
                                            for i in range(5, 11, 5):
                                                traintimes[13] = (datetime.time(9,35+i,0)) 
                                                for i in range(5, 11, 5):
                                                    traintimes[14] = (datetime.time(9,45+i,0)) 
                                                    traintimes[15] = (datetime.time(10,0,0))
                                                    trainType = ['L4', 'L8', 'L8','L8','L8','L8','L8','L8','L8','L8','L8','L8','L8','L4','L4','L4',]
                                                    
                                                    if sorted(traintimes) == traintimes:
                                                        null = [datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
                                                                datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
                                                                datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0),
                                                                datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0), datetime.time(0, 0, 0)]

                                                        d = {'TrainNum': null,
                                                             'TrainType': null,
                                                             'Total_Wait_Time': null,
                                                             'A_ArrivalTime': null,
                                                             'A_DepartureTime': null,
                                                             'A_AvailCap': null,
                                                             'A_Boarding': null,
                                                             'B_ArrivalTime': null,
                                                             'B_AvailCap': null,
                                                             'B_Boarding': null,
                                                             'B_DepartureTime': null,
                                                             'B_Leftover_End': null,
                                                             'B_NewArrivals': null,
                                                             'C_ArrivalTime': null,
                                                             'C_AvailCap': null,
                                                             'C_Boarding': null,
                                                             'C_DepartureTime': null,
                                                             'C_Leftover_Init': null,
                                                             'C_Leftover_End': null,
                                                             'C_NewArrivals': null,
                                                             'U_Arrival': null,
                                                             'U_AvailCap': null,
                                                             'U_Offloading': null}

                                                        df = pd.DataFrame(data=d)
                                                        df["TrainType"] = trainType

                                                        """
                                                        d = {'TrainNum': trainNum,
                                                             'TrainType': trainType,
                                                             'Total_Wait_Time': null,
                                                             'A_ArrivalTime': a_arrival_time,
                                                             'A_DepartureTime': a_departure_time,
                                                             'A_AvailCap': a_availcap,
                                                             'A_Boarding': A_boarding,
                                                             'B_ArrivalTime': b_arrival_time,
                                                             'B_AvailCap': b_availcap,
                                                             'B_Boarding': B_boarding,
                                                             'B_DepartureTime': b_departure_time,
                                                             'B_Leftover_End': B_Leftover_End,
                                                             'B_NewArrivals': B_Arrivals,
                                                             'C_ArrivalTime': c_arrival_time,
                                                             'C_AvailCap': c_availcap,
                                                             'C_Boarding': C_boarding,
                                                             'C_DepartureTime': c_departure_time,
                                                             'C_Leftover_Init': null,
                                                             'C_Leftover_End': null,
                                                             'C_NewArrivals': null,
                                                             'U_Arrival': u_arrival_time,
                                                             'U_AvailCap': null,
                                                             'U_Offloading': null}
                                                        """

                                                        times = pd.DataFrame(data={
                                                            'Time': [(datetime.datetime.combine(datetime.date(1, 1, 1), time(7, 0, 0)) + timedelta(minutes=x * 10)).time() for x
                                                                     in range(19)],
                                                            'APassengers': [25, 50, 75, 100, 125, 150, 125, 100, 75, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
                                                            'BPassengers': [50, 75, 100, 125, 150, 175, 150, 125, 100, 100, 75, 75, 50, 45, 35, 25, 20, 15, 10],
                                                            'CPassengers': [50, 100, 150, 200, 250, 200, 175, 150, 150, 125, 100, 75, 50, 50, 45, 40, 35, 30, 25]})

                                                        # TrainNum
                                                        trainNum = []
                                                        for i in range(1, 17):
                                                            trainNum.append(i)
                                                        df['TrainNum'] = trainNum

                                                        # A_ArrivalTime
                                                        aArrivalTime = [datetime.time(7, 0, 0), datetime.time(7, 10, 0), datetime.time(7, 15, 0), datetime.time(7, 20, 0),
                                                                        datetime.time(7, 30, 0), datetime.time(7, 40, 0), datetime.time(7, 50, 0), datetime.time(8, 0, 0),
                                                                        datetime.time(8, 10, 0), datetime.time(8, 20, 0), datetime.time(8, 30, 0), datetime.time(8, 45, 0),
                                                                        datetime.time(9, 10, 0), datetime.time(9, 30, 0), datetime.time(9, 40, 0), datetime.time(10, 0, 0)]
                                                        df['trainType'] = ['L4', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L8', 'L4', 'L4', 'L4', ]
                                                        a_arrival_time = aArrivalTime
                                                        df['A_ArrivalTime'] = a_arrival_time

                                                        # A_DepartureTime
                                                        a_departure_time = []
                                                        for i in a_arrival_time:
                                                            a_departure_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=3)).time())
                                                        df['A_DepartureTime'] = a_departure_time

                                                        # A_Boarding
                                                        A_boarding = []
                                                        i = 0
                                                        j = 0
                                                        sum = 0
                                                        lastdep = datetime.time(6, 0, 0)
                                                        newdep = df["A_DepartureTime"].iloc[j]
                                                        while i < 19:
                                                            line = times['Time'].iloc[i]
                                                            if lastdep < line <= newdep:
                                                                sum += times['APassengers'].iloc[i]
                                                                i += 1

                                                            else:
                                                                A_boarding.append(sum)
                                                                sum = 0
                                                                lastdep = newdep

                                                                if j < 15:
                                                                    j += 1
                                                                newdep = df['A_DepartureTime'].iloc[j]

                                                        if len(A_boarding) < 16:
                                                            A_boarding.append(sum)
                                                        df['A_Boarding'] = A_boarding


                                                        # A_Avail_Cap
                                                        a_availcap = []
                                                        for cap in df['TrainType']:
                                                            if cap == 'L4':
                                                                a_availcap.append(200)
                                                            else:
                                                                a_availcap.append(400)
                                                        df['A_AvailCap'] = a_availcap

                                                        # B_ArrivalTime
                                                        b_arrival_time = []
                                                        for i in a_arrival_time:
                                                            b_arrival_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=11)).time())
                                                        df['B_ArrivalTime'] = b_arrival_time

                                                        # B_DepartureTime
                                                        b_departure_time = []
                                                        for i in b_arrival_time:
                                                            b_departure_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=3)).time())
                                                        df['B_DepartureTime'] = b_departure_time

                                                        # B_Avail_Cap
                                                        b_availcap = np.array(a_availcap) - np.array(A_boarding)
                                                        df['B_AvailCap'] = b_availcap

                                                        # B Boarding
                                                        B_Arrivals = []
                                                        i = 0
                                                        j = 0
                                                        sum = 0
                                                        lastdep = datetime.time(6, 0, 0)
                                                        newdep = df["B_DepartureTime"].iloc[j]
                                                        while i < 19:
                                                            line = times['Time'].iloc[i]
                                                            if line > lastdep and line <= newdep:
                                                                sum += times['BPassengers'].iloc[i]
                                                                i += 1

                                                            else:
                                                                B_Arrivals.append(sum)
                                                                sum = 0
                                                                lastdep = newdep

                                                                if j < 15:
                                                                    j += 1
                                                                newdep = df['B_DepartureTime'].iloc[j]
                                                        if len(B_Arrivals) < 16:
                                                            B_Arrivals.append(sum)


                                                        B_boarding = [min(B_Arrivals[0], b_availcap[0])]

                                                        B_Leftover_End = [max(0, B_boarding[0] - b_availcap[0])]

                                                        for i in range(1, 15):
                                                            B_boarding.append(min(B_Leftover_End[i - 1] + B_Arrivals[i], b_availcap[i]))
                                                            B_Leftover_End.append(B_Leftover_End[i - 1] + B_Arrivals[i] - B_boarding[i])

                                                        if len(B_boarding) < 16:
                                                            B_boarding.append(B_Leftover_End[14] + B_Arrivals[15])
                                                        B_Leftover_End.append(0)

                                                        df['B_Boarding'] = B_boarding

                                                        # C_ArrivalTime
                                                        c_arrival_time = []
                                                        for i in b_arrival_time:
                                                            c_arrival_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=12)).time())
                                                        df['C_ArrivalTime'] = c_arrival_time

                                                        # C_DepartureTime
                                                        c_departure_time = []
                                                        for i in c_arrival_time:
                                                            c_departure_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=3)).time())
                                                        df['C_DepartureTime'] = c_departure_time

                                                        # C_availcap
                                                        c_availcap = np.array(b_availcap) - np.array(B_boarding)
                                                        df['C_AvailCap'] = c_availcap

                                                        # C Boarding
                                                        # PLEASE NOTE WE USED ARRIVAL TIME HERE INSTEAD OF DEPARTURE TIME!!
                                                        C_Arrivals = []
                                                        i = 0
                                                        j = 0
                                                        sum = 0
                                                        lastdep = datetime.time(6, 0, 0)
                                                        newdep = df["C_ArrivalTime"].iloc[j]
                                                        while i < 19:
                                                            line = times['Time'].iloc[i]
                                                            if line > lastdep and line <= newdep:
                                                                sum += times['CPassengers'].iloc[i]
                                                                i += 1

                                                            else:
                                                                C_Arrivals.append(sum)
                                                                sum = 0
                                                                lastdep = newdep

                                                                if j < 15:
                                                                    j += 1
                                                                newdep = df['C_ArrivalTime'].iloc[j]

                                                        while len(C_Arrivals) < 16:
                                                            C_Arrivals.append(sum)
                                                            sum = 0


                                                        C_boarding = [min(C_Arrivals[0], c_availcap[0])]

                                                        C_Leftover_End = [max(0, C_Arrivals[0] - C_boarding[0])]

                                                        for i in range(1, 15):
                                                            C_boarding.append(min(C_Leftover_End[i - 1] + C_Arrivals[i], c_availcap[i]))
                                                            C_Leftover_End.append(C_Leftover_End[i - 1] + C_Arrivals[i] - C_boarding[i])

                                                        if len(C_boarding) < 16:
                                                            C_boarding.append(C_Leftover_End[14] + C_Arrivals[15])
                                                        C_Leftover_End.append(0)

                                                        df['C_Boarding'] = C_boarding

                                                        # U_ArrivalTime
                                                        u_arrival_time = []
                                                        for i in c_arrival_time:
                                                            u_arrival_time.append((datetime.datetime.combine(datetime.date(1, 1, 1), i) + timedelta(minutes=14)).time())
                                                        df['U_Arrival'] = u_arrival_time

                                                        # TotalWaitTime
                                                        # = Total Wait + A wait + B wait + C wait
                                                        cumWait = 0
                                                        i = 0
                                                        j = 0
                                                        lastdep = datetime.time(6, 0, 0)
                                                        newdep = df["C_ArrivalTime"].iloc[j]
                                                        # loop over sets of departures
                                                        while i < 19:
                                                            line = times['Time'].iloc[i]
                                                            if line > lastdep and line <= newdep:
                                                                cumWait += times['APassengers'].iloc[i] * int(((datetime.datetime.combine(date.today(), newdep) - datetime.datetime.combine(date.today(), line)).total_seconds())/60)
                                                                i += 1
                                                            else:
                                                                lastdep = newdep
                                                                if j < 15:
                                                                    j += 1
                                                                newdep = df['A_ArrivalTime'].iloc[j]


                                                        i = 15
                                                        j = 18

                                                        bBoard = np.sum(df['B_Boarding'])
                                                        recentArr = times['BPassengers'].iloc[j]
                                                        recentBoard = df['B_Boarding'].iloc[i]

                                                        while bBoard > 0:

                                                            if recentArr > recentBoard:
                                                                cumWait += recentBoard * (datetime.datetime.combine(date.today(), df['B_DepartureTime'].iloc[i]) - datetime.datetime.combine(date.today(), times['Time'].iloc[j])).total_seconds()/60
                                                                recentArr -= recentBoard
                                                                bBoard -= df['B_Boarding'].iloc[i]
                                                                i -= 1
                                
                                                                recentBoard = df['B_Boarding'].iloc[i]
                                                            else:
                                                                cumWait += recentArr * (datetime.datetime.combine(date.today(), df['B_DepartureTime'].iloc[i]) - datetime.datetime.combine(date.today(), times['Time'].iloc[j])).total_seconds()/60
                                                                bBoard -= recentArr
                                                                recentBoard -= recentArr
                                                                j -= 1
                                                                recentArr = times['BPassengers'].iloc[j]




                                                        i = 15
                                                        j = 18

                                                        cBoard = np.sum(df['C_Boarding'])
                                                        recentArr = times['CPassengers'].iloc[j]
                                                        recentBoard = df['C_Boarding'].iloc[i]

                                                        while cBoard > 0:

                                                            if recentArr > recentBoard:
                                                                cumWait += recentBoard * (datetime.datetime.combine(date.today(), df['C_DepartureTime'].iloc[i]) - datetime.datetime.combine(date.today(), times['Time'].iloc[j])).total_seconds()/60
                                                                recentArr -= recentBoard
                                                                cBoard -= df['C_Boarding'].iloc[i]
                                                                i -= 1
                                                                recentBoard = df['C_Boarding'].iloc[i]
                                                            else:
                                                                cumWait += recentArr * (datetime.datetime.combine(date.today(), df['C_DepartureTime'].iloc[i]) - datetime.datetime.combine(date.today(), times['Time'].iloc[j])).total_seconds()/60
                                                                cBoard -= recentArr
                                                                recentBoard -= recentArr
                                                                j -= 1
                                                                recentArr = times['CPassengers'].iloc[j]
                                                        # add U-
                                                        

                                                        cur_time = cumWait
                                                        if cur_time < best_time:
                                                            best_time = cur_time
                                                            best = traintimes

                                                        """
                                                        traintimes = [
                                                        datetime.time(7,0,0),
                                                        datetime.time(7,10,0),
                                                        datetime.time(7,15,0),
                                                        datetime.time(7,20,0),
                                                        datetime.time(7,30,0),
                                                        datetime.time(7,40,0),
                                                        datetime.time(7,50,0),
                                                        datetime.time(8,0,0),
                                                        datetime.time(8,10,0),
                                                        datetime.time(8,20,0),
                                                        datetime.time(8,30,0),
                                                        datetime.time(8,45,0),
                                                        datetime.time(9,10,0),
                                                        datetime.time(9,30,0)
                                                        ,datetime.time(9,40,0),
                                                        datetime.time(10,0,0)]
                                                        """



print(best)
print(best_time)
print("Average wait time: " + str(best_time/4600))
df.to_csv("moment1.csv")