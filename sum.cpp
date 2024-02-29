#include <iostream>
#include <chrono>
unsigned sum(int data[], unsigned size, int key){
    for(int i=0;i<size;i++){
        for(int j=1;j<size;j++)
        if(data[i]+data[j]==key)
        return i+j;
    }
    return size;
}
int main(){
    unsigned n=2000;
    
    for(unsigned j=500;j<=n;j += 500){
        int *data = new int[j];
        for(unsigned i=0;i<j-1;i++)
            data[i]=i;
        int x;
        srand(time(0));
        x=rand()%j;
        auto begin = std::chrono::steady_clock::now();
        for (unsigned cnt = 100000; cnt!=0; --cnt)
            sum(data, j, x);
        auto end = std::chrono::steady_clock::now();
        auto time_span = std::chrono::duration_cast<std::chrono::milliseconds>(end - begin);
    
        
        std::cout <<time_span.count()<<std::endl;
    }
    std::cout<<"finish";
    return 0;
    
}