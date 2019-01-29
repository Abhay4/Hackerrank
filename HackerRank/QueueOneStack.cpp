#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void enque(stack<int> &s, int val)
{
    s.push(val);
}

void print(stack<int> s){
    if(s.empty()){
        return;
    }
    int x = s.top();
    s.pop();
    print(s);
    cout<<x<<" ";
    
}
bool dequeue(stack<int> &s)
{
    if(s.empty())
        return true;
    int x = s.top();
    s.pop();
    if(dequeue(s)){
        return false;
    };
    s.push(x);
    return false;
}

int main()
{
   stack<int> s; 
   enque(s,1);
   enque(s,2);
   enque(s,3);
   enque(s,4);
   print(s);
   cout<<endl;
   bool x =dequeue(s);
   print(s);
   
   cout<<endl;
   x =dequeue(s);
   print(s);
   
   cout<<endl;
   enque(s,5);
   print(s);
   
   
   return 0;
}