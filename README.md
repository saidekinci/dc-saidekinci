# dc-saidekinci

Data 1202 Assignment 5

1. I have used the data from our previous assignment which was the youtube_dataset.


2. The library used is pandas

df = pd.read_csv('C:/Users/ekinc/OneDrive/Desktop/youtube_dataset.csv')


3. Then I have displayed the first 5 rows to check if I have the right type of data in.

df.head()


4. By using th iloc command I have selected the first 1000 entries. 

def slice_data (df, number_of_rows):
    return df.iloc[:number_of_rows]
first_1000 = slice_data(df, 1000)


5. I have used the below code to display the channel type as a list.

new_hist= pd.DataFrame(list(hist.items()),columns = ['ChannelType','Count']) 
new_hist


6. I also used the below code to display the channel type as graph to get a nicer picture of it.

plt.figure(figsize=(15,10))
sns.barplot(x='ChannelType', 
            y='Count', 
            data=new_hist, 
            order=new_hist.sort_values('Count',ascending = False).ChannelType)

plt.xlabel("Channel Type", size= 15)
plt.ylabel("Count", size=15)
plt.title("Distribution of Channel type from the top 1000 records including NAs", size=18)
plt.tight_layout()
plt.savefig("Distribution of Channel type from the top 1000 records including NAs", dpi=100)


7. The query below was used to calculate the channel type distribution.

hist = {}

def dist(t):
    for x in t:
        hist[x] = hist.get(x,0) + 1

distrubition = dist(first_1000.channeltype)


8. Finally the new data frame file was saved as CVS.

first_1000.to_csv(r'C:/Users/ekinc/OneDrive/Desktop/youtube1000.csv', index = False)

     
