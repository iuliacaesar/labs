#include <iostream>
#include <chrono>
unsigned binary_search(int data[], unsigned size, int key){
    unsigned l=0, r=size-1;
    while(l<r){
        unsigned mid=(r+l)/2;
        if (key<data[mid]) r=mid;
        else if(key>data[mid]) l=mid+1;
        else return mid;
    }
    return size;
}

int main(){
    
    unsigned n=750000;
    
    for(unsigned j=1;j<=10;j++){
        int *data = new int[n];
        for(unsigned i=0;i<n-1;i++)
            data[i]=i;
        int x;
        srand(time(0));
        x=rand()*rand()%n;
        auto begin = std::chrono::steady_clock::now();
        for (unsigned cnt = 100000; cnt!=0; --cnt)
            binary_search(data, n, x);
        auto end = std::chrono::steady_clock::now();
        auto time_span = std::chrono::duration_cast<std::chrono::microseconds>(end - begin);
    
        //std::cout << "\n\n";
        std::cout <<' '<<time_span.count()<<std::endl;
    }
    std::cout<<"finish";
    return 0;

}