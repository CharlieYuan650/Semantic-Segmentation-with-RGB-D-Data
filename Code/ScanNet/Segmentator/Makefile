CXX = g++
FLAGS=-std=c++11

segmentator: segmentator.cpp tinyply.cpp
	$(CXX) $(FLAGS) -o segmentator segmentator.cpp tinyply.cpp

clean:
	rm -f *~ *.o segmentator

.PHONY: clean