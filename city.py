import numpy as np
import random


class City:
    #City needs to create pattern, check pattern, then recreate pattern
    #City needs incentive variable & check
    #City needs pattern_recreate_normalization_delta for joining roads.
    def __init__(self):
        self.city = []
        self.createGrid()
        self.initPattern()


    def createGrid(self):
        '''A quick reference for city-array indices:
        city[y,x] will give you a city sector;
        city[y,x][:nY,:nX] is the technique
        for row or column based operation
        inside that sector.'''

        for _s in range(3):
            #large sectors
            sector = []

            for _m in range(4):
                #inner sectors; "square miles"
                sq_mile = np.zeros((12,12))
                sector.append(sq_mile)

            sector = np.array(sector)
            self.city.append(sector)

        self.city = np.array(self.city)

    def initPattern(self):
        row = 0
        for item in self.city:
            print("ROW {}".format(row))
            column = 0
            for _i in item:
                print("COLUMN {}".format(column))
                self.createPattern(row=row,col=column)
                column += 1
            row += 1

    def createPattern(self, row=None, col=None):
        #Should introduce an "incentive" check in the form  'if incentive//1:'
        #where incentive is a float and the increments are decimals
        '''This section is for randomly choosing the foundation for a "sq_mile"
        road network. The results should be pointers to information for
        where to create the road, how far the road extends, and in which way
        the road is oriented [H,V,D]. It should also be determined if a road has
        sub-branching routes or not.'''

        num_roads = random.choice([2,3])


        for _ in range(num_roads):
            road_orientation = random.choice([0,1,2])
            #print("Pattern Does Branch? {}".format(bool(does_branch)))


            #a horizontal road
            if road_orientation == 0:
                road_position = random.randrange(1, len(self.city[0,0]))
                #print("Pattern Horizontal Road {}".format(road_position))
                self.createRoads(self.city[row][col], vector= road_position, orientation='h')

            #a vertical road
            elif road_orientation == 1:
                road_position = random.randrange(1, len(self.city[0,0][0]))
                #print("Pattern Vertical Road {}".format(road_position))
                self.createRoads(self.city[row][col], vector= road_position, orientation='v')

            #a diagonal road
            else:
                _orient_self = random.choice([0,1])

                if _orient_self:
                    road_position = -random.randrange(1, len(self.city[0,0])//2)
                    #print("Pattern Diagonal, vertical off-set {}".format(road_position))

                else:
                    road_position = random.randrange(1, len(self.city[0,0][0])//2)
                    #print("Pattern Diagonal, horizontal off-set {}".format(road_position))

                self.createRoads(self.city[row][col],vector=road_position,orientation='d')

        return print("Pattern Ran.")

    def createRoads(self,array,vector=None,orientation=None,):
        '''A quick reference for roads:
        Refer to city indices for element-based modifications,
        the following code produces a road-like pattern by choosing
        random numbers with a range of the size of the path. The road
        should either be a linear vector, a horizontal vector, or a np.eye.
        '''
        try:
            orientation = orientation.lower().strip()

        except:
            return print("Invalid Operation.\nUse 'v'(vertical), 'h'(horizontal), 'd'(diagonal)")

        #vertical road method:
        #city[y,x,:length_road, road_position] += 1
        if orientation == 'v':
            array[:,vector-1] += 1
            pass
        #horizontal road method:
        #city[y,x,road_position, :length_road] += 1
        if orientation == 'h':
            array[vector-1] += 1
            pass
        #diagonal road method:
        #city[y,x] += np.eye[shape(city,size[y,x])]
        if orientation == 'd':
            eye = np.eye(*array.shape,k=vector)
            invert_array = random.choice([0,1])
            if invert_array:
                #1 is y, 0 is x
                mirror_axis = random.choice([0,1])
                if mirror_axis:
                    eye = eye[::-1,:]
                else:
                    eye = eye[:,::-1]
            else:
                pass
            array += eye
            pass

    def validateCity(self):
        '''This section is for taking the created city, checking the outlets of
        each road, comparing against the neighboring arrays and seeing if a valid
        connection is made. If there isn't, one is created in
        the original array or the neighboring array'''

        row = 1
        for _i in self.city:
            col = 1
            for _ in _i:
                print("INDEX ROW: {} COL: {}".format(row,col))
                values = np.where(_ > 0)
                values = [*zip(*values)]
                col += 1
                print(values)
            row += 1
        pass
    def printcity(self):
        #return print(self.city)
        for _i in self.city:
            print(_i)

    def showcity(self):
        #plot all the individual elements of the City

        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(*self.city.shape[:2])
        row = 0
        for _i in self.city:
            col = 0
            for _ in _i:
                ax= axs[row,col]
                ax.spy(_, markersize=5)
                ax.set_xticks([])
                ax.set_yticks([])
                col += 1
            row += 1
        plt.subplots_adjust(wspace=0,hspace=0)
        plt.show()







city = City()

#city.printcity()
city.validateCity()
city.showcity()


print(city.city.shape)
