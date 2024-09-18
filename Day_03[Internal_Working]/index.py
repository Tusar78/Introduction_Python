# myListOne = [1,2,3];
# myListTwo = myListOne;
# myListOne[1] = "Rakib";
# print(myListTwo);

# x = [1,2,3];
# y = x[:];
# print(x);
# x[0] = "Rakib"
# print(x)
# print(y);

import copy

# x = [10,20,30, ["rakib", "Tusar"]];
# y = x.copy();
# x[3:] = "1";
# print(x);
# print(y);

x = [1,2,3]; 
y = [1,2,3];
print(x == y);

