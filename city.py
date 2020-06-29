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
        self.empty_arrays = []
        self.validation_dict = {}


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
                sq_mile = np.zeros((16,16))
                sector.append(sq_mile)

            sector = np.array(sector)
            self.city.append(sector)

        self.city = np.array(self.city)

    def initPattern(self):
        row = 0
        #even = 0, odd = 1
        #Sets the pattern for city creation
        even_or_odd = random.choice([0,1])
        for item in self.city:

            column = 0
            if even_or_odd:

                for _i in item:
                    if column % 2 == 1:
                        self.createPattern(row=row,col=column)

                    else: pass
                    column += 1

                row += 1
                even_or_odd -= 1
            else:

                for _i in item:
                    if column % 2 == 0:
                        self.createPattern(row=row,col=column)

                    else: pass
                    column += 1

                row += 1
                even_or_odd += 1


    def createPattern(self, row=None, col=None):
        #Should introduce an "incentive" check in the form  'if incentive//1:'
        #where incentive is a float and the increments are decimals
        '''This section is for randomly choosing the foundation for a "sq_mile"
        road network. The results should be pointers to information for
        where to create the road, how far the road extends, and in which way
        the road is oriented [H,V,D]. It should also be determined if a road has
        sub-branching routes or not.'''

        num_roads = len(self.city[0,0])//4

        for _ in range(num_roads):

            road_orientation = random.choice([0,1,2])

            #a horizontal road
            if road_orientation == 0:
                road_position = random.randrange(1, len(self.city[0,0]))
                self.createRoads(self.city[row][col], vector= road_position, orientation='h')

            #a vertical road
            elif road_orientation == 1:
                road_position = random.randrange(1, len(self.city[0,0][0]))
                self.createRoads(self.city[row][col], vector= road_position, orientation='v')

            #a diagonal road
            else:
                _orient_self = random.choice([0,1])

                if _orient_self:
                    road_position = -random.randrange(1, len(self.city[0,0])//2)

                else:
                    road_position = random.randrange(1, len(self.city[0,0][0])//2)

                self.createRoads(self.city[row][col],vector=road_position,orientation='d')

    def createRoads(self,array,vector=None,orientation=None,):
        '''A quick reference for roads:
        Refer to city indices for element-based modifications,
        the following code produces a road-like pattern by choosing
        random numbers with a range of the size of the path. The road
        should either be a column vector, a row vector, or a np.eye.
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
        '''This segment is for populating the validation_dict with outlets from the
        sections of self.city that were randomly created. The empty_arrays list is
        also updated. The results will be used to make connections between the two or
        more city sections.'''

        row = 0
        for _i in self.city:

            col = 0
            for _ in _i:
                values = np.where(_ > 0)
                values = [*zip(*values)]

                if values:
                    values = [i for i in values if np.max(values) in i or np.min(values) in i]
                    self.validation_dict[(row,col)] = values

                else: self.empty_arrays.append((row,col))

                col += 1
            row += 1
        self.find_connections()


    def find_connections(self):
        open_connections = {}
        for k_index in self.empty_arrays:
            y,x = k_index
            print("Now Checking Area:", k_index)
            #A KeyError signifies that we've reached the edge of the city
            try:
                val_up = self.validation_dict[(y-1,x)].copy()
                val_up = [i for i in val_up if i[0] == len(self.city[y,x])-1]

                #print("Up Index",val)
            except KeyError:
                val_up = []
                pass

            if val_up:
                open_connections["U"] = val_up


            try:
                val_dwn = self.validation_dict[(y+1,x)].copy()
                val_dwn = [i for i in val_dwn if i[0] == 0]

                #print("Down Index", val)
            except KeyError:
                val_dwn = []
                pass

            if val_dwn:
                open_connections["D"] = val_dwn


            try:
                val_lft = self.validation_dict[(y,x-1)].copy()
                val_lft = [i for i in val_lft if i[1] == len(self.city[y,x][0])-1]

                #print("Left Index", val)
            except KeyError:
                val_lft = []
                pass

            if val_lft:
                open_connections["L"] = val_lft

            try:
                val_rgt = self.validation_dict[(y,x+1)].copy()
                val_rgt = [i for i in val_rgt if i[1] ==0]

                #print("Right Index", val)
            except KeyError:
                val_rgt = []
                pass
            if val_rgt:
                open_connections["R"] = val_rgt


            self.connectDots(open_connections)

    def connectDots(self, dots=None):
        print(dots)

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
                ax.spy(_, markersize=7)
                ax.set_xticks([])
                ax.set_yticks([])
                col += 1
            row += 1
        #-preset config for display
        plt.subplots_adjust(wspace=0,hspace=0)
        plt.subplots_adjust(left=0.22,bottom=0.05,right=0.85,top=0.94)
        #-auto fullscreen
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')

        plt.show()

if __name__ == "__main__":
    city = City()
    city.validateCity()
    city.showcity()

