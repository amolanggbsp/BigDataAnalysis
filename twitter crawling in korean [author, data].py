import pandas as pd
import csv



with open('CrwaledText.csv', 'w', newline='',encoding='UTF8', errors='ignore') as f:

    writer = csv.writer(f)
    writer.writerow( ['Text', 'Writer[id]','Posted Date'] ) 
    
       # Read excel file and store values in Pandas "DataFrame" variable
    df=pd.read_excel('Twitter Crawling.xlsx', 'Sheet1', encoding='UTF8',errors='ignore')


    # Get the index location of all "More" text in our file.
    # Converts the value to a list for later use
    indexes = df[df["키보드 단축키"] == '더 보기'].index.tolist()

    for index in indexes:
        # iloc[row, column] retunrs the value of the specified cell 
        # by "row" and "column" values
        b=(df.iloc[index-1,0])
        a=(df.iloc[index+1,0])
        author=str(b)
        text=str(a)
        
        if 'Replying to' in text:
            a=(df.iloc[index+1,0]+"         "+df.iloc[index+2,0])

        s2='@'
        if s2 in b:
            c=b[b.index(s2) + len(s2):]

            date=c[-6::1]
            author=c[0:-6:1]

            if "rs ago" in date:
                    date=c[-6::1]
                    author=c[0:-6:1]


            
      
         
            
            
      
  
        print(a)
        print('.......')
        print(date)
        print('.......')
        print(author)
        print ('----------------------------------------')

        Field1=a
        Field3=date
        Field2=author


        writer.writerow([Field1,Field2,Field3])
        
        
        



#print(df)
#print(indexes)
