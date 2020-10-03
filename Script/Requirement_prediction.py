import csv
import json
from collections import defaultdict as ddict

wd = "./" # The directory that the data files are in

user_ke_profiles = ddict(list)
job_ke_users = ddict(list)
user_ke_predicted_profiles = ddict(lambda: ddict(list))
print "Recording profile loc"
job_info = {}
with open(wd + "./data/", "r") as infile:
    reader = csv.reader(infile, delimiter="\t", 
    quoting=csv.QUOTE_NONE, quotechar="")
    reader.next() 
    for line in reader:
        (UserID, JobTitle, Requirements, City, State, 
        Country,Education,Skills) = line
        job_info[str(Userid)] = [int(JobTitle), State, City, 0] #input : {users ID,Location , Keywords , Education ,JobTitle(if present ) ,other mentioned details if present 
#Change the input parameters names as per your requirement 
#You can remove or add any data input in the above mentioned format
print "Counting applications..."
with open(wd + "./data/..") as infile:
    reader = csv.reader(infile, delimiter="\t")
    reader.next()
    for line in reader:
        (UserId,  Split,JobTitle) = line
        if WindowID == 2: break
        user_ke_jobs[UserId].append(JobTitle)
        job_ke_users[JobTitle].append(UserId)

print "Finding similar Profiles"
with open(wd + "./data/...", "r") as infile:
    reader = csv.reader(infile, delimiter="\t", 
    quoting=csv.QUOTE_NONE, quotechar="")
    reader.next() 
    for line in reader:
        (UserId, WindowId, Split, City, State, Country, ZipCode,
        DegreeType, Major, GraduationDate, WorkHistoryCount,
        TotalYearsExperience, CurrentlyEmployed, ManagedOthers,
        ManagedHowMany) = line
        if Split == "Train":
            continue
        for profile_id in user_ke_jobs[UserId]:
           for user_id1 in profile_ke_users[job_id]:
              for profile_id1 in user_ke_profiles[user_id1]:
                 if profile_id1 in user_ke_profiles[UserId]: break
                 if user_ke_predicted_profiles[UserId].has_key(job_id1):
                    user_ke_predicted_profiles[UserId][job_id1] += 1
                 else:
                    user_ke_predicted_profiles[UserId][job_id1] = 1

print "Sorting collaborative filtering Profiles..."
predicted_profiles_tuples = ddict(list)
for user_id in user_ke_predicted_profiles.keys():
   for job_id, count in user_ke_predicted_profiles[user_id].items():
      predicted_profiles_tuples[user_id].append((job_id, count))
   predicted_profiles_tuples[user_id].sort(key=lambda x: x[1])
   predicted_profiles_tuples[user_id].reverse()

print "Sorting profiles on based on needs..."
top_city_profiles = ddict(lambda: ddict(lambda: ddict(list)))
top_state_profiles = ddict(lambda: ddict(list))
for (job_id, (window, State, City, count)) in job_info.items():
    top_city_profiles[window][State][City].append((job_id, count))
    top_state_profiles[window][State].append((job_id, count))
for window in [1]:
    for state in top_city_profiles[window]:
        for city in top_city_profiles[window][state]:
            top_city_profiles[window][state][city].sort(key=lambda x: x[1])
            top_city_profiles[window][state][city].reverse()
    for state in top_state_profiles[window]:
        top_state_profiles[window][state].sort(key=lambda x: x[1])
        top_state_profiles[window][state].reverse()

print "Making predictions..."
with open(wd + "./data/users.tsv", "r") as infile:
    reader = csv.reader(infile, delimiter="\t", 
    quoting=csv.QUOTE_NONE, quotechar="")
    reader.next() # burn the header
    with open("./result/popular_jobs1.csv", "w") as outfile:
        outfile.write("UserId, JobIds\n")
        for line in reader:
            (UserId, WindowId, Split, City, State, Country, ZipCode,
            DegreeType, Major, GraduationDate, WorkHistoryCount,
            TotalYearsExperience, CurrentlyEmployed, ManagedOthers,
            ManagedHowMany) = line
            if Split == "Train":
                continue
            top_profiles = predicted_profiles_tuples[UserId]
            if len(top_profiles) < 150:
               top_profiles += top_city_profiles[int(WindowId)][State][City]
            if len(top_profiles) < 150:
                top_profiles += top_state_jobs[int(WindowId)][State]
            top_profiles = top_profiles[0:150]
            outfile.write(str(UserId) + "," + " ".join([x[0] for x in top_profiles]) + "\n")
