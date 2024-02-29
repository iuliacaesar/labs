#include <iostream>
#include <chrono>
unsigned search(int data[], int key, unsigned size){
    unsigned i=0;
    while(data[i]!=key && i<size)
    i++;
    return i;
}
int main(){
    unsigned n=1000000;
    
    for(unsigned j=50000;j<=n;j += 50000){
        int *data = new int[j];
        for(unsigned i=0;i<j-1;i++)
            data[i]=1;
        //int x;
        //srand(time(0));
        //x=rand()*rand()%j;
        auto begin = std::chrono::steady_clock::now();
        for (unsigned cnt = 100000; cnt!=0; --cnt)
            search(data, 2, j);
        auto end = std::chrono::steady_clock::now();
        auto time_span = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin);
    
        
        std::cout<<time_span.count()<<std::endl;
    }
    std::cout<<"finish";
    return 0;
    
}