#include <iostream>
#include <chrono>
unsigned sum(int data[], unsigned size, int key){
    unsigned l=0, r=size-1;
    while(data[l]+data[r]!=key && l<r){
        if(data[l]+data[r]>key)
        r -= 1;
        if(data[l]+data[r]<key)
        l += 1;
    }
    return l+r;
}
int main(){
    unsigned n=2000;
    
    for(unsigned j=500;j<=n;j += 500){
        int *data = new int[j];
        for(unsigned i=0;i<j-1;i++)
            data[i]=1;
        //int x;
        //srand(time(0));
        //x=rand()*rand()%j;
        auto begin = std::chrono::steady_clock::now();
        for (unsigned cnt = 100000; cnt!=0; --cnt)
            sum(data, j, 3);
        auto end = std::chrono::steady_clock::now();
        auto time_span = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin);
    
        std::cout << "\n\n";
        std::cout <<time_span.count()<<std::endl;
    }
    std::cout<<"finish";
    return 0;
    
}