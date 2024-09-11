import matplotlib.pyplot as plt

world_records = {
    'humans':{
    1912: {'athlete': "Donald Lippincott", 'time': "10.6 seconds"},
    1920: {'athlete': "Charles Paddock", 'time': "10.4 seconds"},
    1930: {'athlete': "Percy Williams", 'time': "10.3 seconds"},
    1936: {'athlete': "Jesse Owens", 'time': "10.2 seconds"},
    1956: {'athlete': "Willie Williams", 'time': "10.1 seconds"},
    1968: {'athlete': "Jim Hines", 'time': "9.95 seconds"},
    1983: {'athlete': "Calvin Smith", 'time': "9.93 seconds"},
    1988: {'athlete': "Carl Lewis", 'time': "9.92 seconds"},
    1991: {'athlete': "Carl Lewis", 'time': "9.86 seconds"},
    1994: {'athlete': "Leroy Burrell", 'time': "9.85 seconds"},
    1996: {'athlete': "Donovan Bailey", 'time': "9.84 seconds"},
    1999: {'athlete': "Maurice Greene", 'time': "9.79 seconds"},
    2005: {'athlete': "Asafa Powell", 'time': "9.77 seconds"},
    2008: {'athlete': "Usain Bolt", 'time': "9.72 seconds"},
    2009: {'athlete': "Usain Bolt", 'time': "9.58 seconds "},
    },
    'lions':{
    2010: {'athlete':"Average lion", 'time':"7.2 second"},
    2011: {'athlete': "Leo", 'time': "7.2 seconds"},
    2012: {'athlete': "Simba", 'time': "7.58 seconds"},
    2013: {'athlete': "Nala", 'time': "7.18 seconds"},
    2014: {'athlete': "Mufasa", 'time': "7.65 seconds"},
    2015: {'athlete': "Zara", 'time': "8.04 seconds"},
    2016: {'athlete': "Marko", 'time': "7.25 seconds"},
    2017: {'athlete': "Mikko", 'time': "7.38 seconds"},
    2018: {'athlete': "Kari", 'time': "7.1 seconds"},
    2019: {'athlete': "Pekka", 'time': "7.00 seconds"},
    2020: {'athlete': "Iiro", 'time': "8.25 seconds"},
    }
}

#years = list(world_records['humans'].keys())
#times = [float(x['time'].split()[0]) for x in world_records['humans'].values()]

#plt.figure(figsize=(10, 5))
#plt.plot(years, times, marker='o', label='100m maailmanennätysten kehitys')

#for year, record in world_records['humans'].items():
#    plt.text(year, float(record['time'].split()[0]), record['athlete'], ha='center', va='bottom')

#plt.title("100m maailmanennätysten kehitys")
#plt.ylabel("Aika (s)", fontsize=12)
#plt.xlabel("Vuosi", fontsize=12)
#plt.grid(True)  
#plt.show() 
