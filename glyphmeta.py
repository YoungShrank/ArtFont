import random
from typing import Iterable
from itertools import product

class Meta:
    def __init__(self) -> None:
        pass
    def make_pairs(self,A:list,B:list,n:int,mapping = "pos"):
        """
        make  pairs of A and B
        - n: int, number of B for each A
        - mapping: the mapping method,default is "pos"
            - pos: by position
            - rand: random
        # returns
        - list[tuple[str,str]] ,length is len(A)*n
        """
        assert mapping in ["pos","rand"]
        for i in range(len(A)):
            if mapping == "pos":
                for j in range(n):
                    yield (A[i],B[(i+j)%len(B)])
            elif mapping == "rand":
                for j in range(n):
                    yield (A[i],random.choice(B))
    def random_tuples(self,n:int,*lists):
        """
        random tuples
        - n:  number of tuples
        - lists : [list],each list is a list of elements
        """
        indices = [list(range(len(i))) for i in lists]
        index_set = set()
        while len(index_set) < n:
            index_set.add(tuple(random.choice(i) for i in indices))

        index = [[lists[i][I[i]] for i in range(len(I)) ] for I in index_set  ]
        return index
        
    def product(self,A:Iterable,B:Iterable):
        """
        product of A and B
        # returns
        - [tuple[str,str]] ,length is len(A)*len(B)
        """
        for a in A:
            for b in B:
                yield (a,b)
class GlyphMeta(Meta):
    def __init__(self,fonts:list[str],colors:list[str],chars:list[str]) -> None:
        super().__init__()
        self.fonts = fonts
        self.colors = colors
        self.chars = chars
    def font_color(self,n:int,mapping = "pos"):
        """
        font and color
        - n: int, number of color for each font
        # returns
        """
        for font,color in self.make_pairs(self.fonts,self.colors,n,mapping):
            yield (font,color)
    def color_font(self,n:int,mapping = "pos" ,reverse = True):
        """
        color and font
        - n: int, number of font for each color
        - reverse: bool, default is True, if True, (font,color)
        # returns
        """
        for color,font in self.make_pairs(self.colors,self.fonts,n,mapping):
            if reverse:
                yield (font,color)
            else:
                yield (color,font)
    def font_color_chars(self,n:int,mapping = "pos"):
        """
        font,color and all chars
        - n: int, number of color for each font
        # returns
        """
        for font,color in self.make_pairs(self.fonts,self.colors,n,mapping):
            for char in self.chars:
                yield (font,color,char)


if __name__ == "__main__":
    meta = GlyphMeta(["font1","font2"],["color1","color2","color3"],["c","p"])
    for f,c,a in meta.font_color_chars(2,"pos"):
        print(f,c,a)
    for i,j,k in meta.random_tuples(100,["a","b","c"]*16,[1,2,3],[1,2,3]):
        print(i,j,k)


    