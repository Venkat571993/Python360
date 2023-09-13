class Time:
    def __init__(self,hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.conversion()

    def addTime(time1,time2):
        total_time = Time(0,0)
        total_time.hours = time1.hours + time2.hours 
        total_time.minutes= time1.minutes + time2.minutes
        total_time.conversion()
        return (total_time)


    def conversion(self): 
        while self.minutes >= 60:
            self.hours +=1
            self.minutes -= 60
        
    
    def displayTime(self):
        print(f"{self.hours}hrs {self.minutes}mins")

    def displayMinutes(self):
        total_minutes= (self.hours * 60) +(self.minutes)
        print(f"Total Minutes: {total_minutes}")



time1 = Time(5,500)
time2 = Time(4,50)
time3 = Time.addTime(time1,time2)

time1.displayTime()
time3.displayTime()
time3.displayMinutes()
        
    
