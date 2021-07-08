'''
/** 
    * Instructions to candidate.
    * 1) Run this code in the REPL to observe its behaviour. The execution entry point is main().
    * 2) Consider adding some additional tests in doTestsPass(). 
    * 3) Implement def shortestPath(self, fromStationName, toStationName)
    method to find shortest path between 2 stations
    * 4) If time permits, some possible follow-ups. 
    */ 
    
/** 
*   Visual representation of the Train map used 
* 
*   King's Cross St Pancras --- Angel ---- Old Street 
*   |                 \                             |
*   |                  \                             |
*   |                   \                             |
*   Russell Square       Farringdon --- Barbican --- Moorgate
*   |                                                /
*   |                                               /
*   |                                              /
*   Holborn --- Chancery Lane --- St Paul's --- Bank
*/
'''
from functools import reduce
import collections
'''
/** 
 * class Station
 * 
 * Respresents Station in the rail network. Each station is identified by
 * unique name. Station is connected with other stations - this information
 * is stored in the 'neighbours' field. Two station objects with the same name are
 * equal therefore they are considered to be same station. 
 */
'''
class Station: 
    def _init_(self, name):
        self._name = name
        self._neighbours = [] 
        
    def getName(self):
        return self._name 
        
    def addNeighbour(self, station):
        self._neighbours.append(station) 
        
    def getNeighbours(self):
        return self._neighbours 
        
    def _ea_(self, other):
        return isinstance(other, Station) and self._name == other.getName() 
        
    def hash (self):
        return hash((self._name)) 
        
''' 
/**
 * class TrainMap 
 * Respresents whole rail network - consists of number of the Station objects
 * Stations in the map are bi-directionally connected. Distance between any 2 stations 
 * is of same constant distance unit. This implies that shortest distance between any 
 * 2 stations depends only on number of stations in between
 */
'''
class TrainMap: 
    def _init_(self):
        self._stations = {}
        
    def addStation(self, stationName):
        self._stations[stationName] = Station(stationName) 
        return self 
        
    def getStation(self, stationName):
        return self._stations[stationName] 
        
    def connectStations(self, fromStation, toStation):
        fromStation.addNeighbour(toStation) 
        toStation.addNeighbour(fromStation) 
        return self 
        
    def convertPathToString(self, path): 
        if(len(path) == 0): 
            return "" 
        else:
            return reduce(lambda sl, s2: sl + "->" + s2, map(lambda station: station.getName(), path)) 
            
    def shortestPath(self, fromStationName, toStationName): 
        fromStation = self. getStation(fromStationName) 
        toStation = self. getStation(toStationName) 
        searchSpace = deque() 
        parentOfNode = {}
        visited = set() 
        
        searchSpace.append(fromStation)
        
        while(len(searchSpace) != 0):
            curr = searchSpace.popleft()
            if(curr not in visited):
            visited.add(curr)
            if(curr == toStation):
                break 
            else: 
                for neighbour in curr.getNeighbours():
                    searchSpace.append(neighbour)
                    if (neighbour not in parentOfNode):
                        parentOfNode[neighbour] = curr 
        parent = parentOfNode[toStation]
        path = [toStation, parent]
        while(parent != fromStation):
            parent = parentOfNode[parent]
            path.append(parent)
        path. reverse()
        return path 
    
def doTestsPass(): 
    # todo: implement more tests, please 
    # feel free to make testing more elegant
    trainMap = TrainMap() 
    trainMap.addStation("King's Cross St Pancras").addStation("Angel").addStation("Old Street").addStation("Moorgate")\ 
    .addStation("Farringdon").addStation("Barbican").addStation("Russel Square").addStation("Holborn")\ 
    .addStation("Chancery Lane").addStation("St Paul's").addStation("Bank") 
    trainMap.connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Angel"))\ 
    .connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Farringdon"))\ 
    .connectStations(trainMap.getStation("King's Cross St Pancras"), trainMap.getStation("Russel Square"))\ 
    .connectStations(trainMap.getStation("Russel Square"), trainMap.getStation("Holborn"))\ .connectStations(trainMap.getStation("Holborn"), trainMap.getStation("Chancery Lane"))\ 
    .connectStations(trainMap.getStation("Chancery Lane"), trainMap.getStation("St Paul's"))\
    .connectStations(trainMap.getStation("St Paul's"), trainMap.getStation("Bank"))\
    .connectStations(trainMap.getStation("Angel"), trainMap.getStation("Old Street"))\ 
    .connectStations(trainMap.getStation("Old Street"), trainMap.getStation("Moorgate"))\ 
    .connectStations(trainMap.getStation("Moorgate"), trainMap.getStation("Bank"))\ 
    .connectStations(trainMap.getStation("Farringdon"), trainMap.getStation("Barbican"))\ 
    .connectStations(trainMap.getStation("Barbican"), trainMap.getStation("Moorgate")) 
    solution = "King's Cross St Pancras->Russel Square->Holborn->Chancery Lane->St Paul's" 
    return solution == trainMap.convertPathToString(trainMap.shortestPath("King's Cross St Pancras", "St Paul's")) 
    
if __name__ =="__main__":
    if(doTestsPass()):
        print('All Tests Pass')
    else:
        print('Some tests fail')
