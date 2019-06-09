import pandas as pd
import csv
import sys



def BMP(s):
        return "".join((i if ord(i) < 10000 else u"\uFFFD" for i in s))



with open('CrwaledText.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow( ['Text', 'Writer[id]','Posted Date'] ) 
    
       # Read excel file and store values in Pandas "DataFrame" variable
    df=pd.read_excel('Twitter Crawling.xlsx', 'Sheet10', encoding='utf8')


    # Get the index location of all "More" text in our file.
    # Converts the value to a list for later use
    indexes = df[df["Keyboard Shortcuts"] == 'More'].index.tolist()

    for index in indexes:
        # iloc[row, column] retunrs the value of the specified cell 
        # by "row" and "column" values
        b=(df.iloc[index-1,0])
        a=(df.iloc[index+1,0])
        author=str(b)
        text=str(a)
        
        if 'Retweet' in text:
            a=(df.iloc[index+1,0]+"         "+df.iloc[index+2,0])

        s2='@'
        if s2 in b:
            c=b[b.index(s2) + len(s2):]

            date=c[-6::1]
            author=c[0:-6:1]

            if date =="rs ago":
                    date=c[-15::1]
                    author=c[0:-15:1]
            if date[2]=='2':
                    date=c[-11::1]
                    author=c[0:-11:1]


            
      
         
            
            
      
  
        print(BMP(a))
        print('.......')
        print(BMP(date))
        print('.......')
        print(BMP(author))
        print ('----------------------------------------')

        Field1=BMP(a)
        Field3=BMP(date)
        Field2=BMP(author)


        writer.writerow([Field1,Field2,Field3])
        
        
        



#print(df)
#print(indexes)

