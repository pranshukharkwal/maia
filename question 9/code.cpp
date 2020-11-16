#include<bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> vvi;
typedef vector<vector<bool>> vvb;
#define endl "\n"
#define PB push_back
#define ll long long
#define FIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

int recur(int i , int j , int count,int h, int w, vvb &graph , vvb &visited){
    visited[i][j] = 1;

    int code1 = 0, code2 = 0;

    // cout<<i<<" "<<j<<endl;
    if(i == h-1 and j == w-1){
        if(count == 0) {
            visited[i][j] = 0; 
            code2 = recur(0,0,1,h,w,graph,visited);  
        }
        else return 2;
    }
    
    //Going down
    if(i != h-1 and graph[i+1][j] and !visited[i+1][j]){
        code1 = recur(i+1 , j , count , h , w , graph, visited);
        if(code1 == 2) return 2;
    }

    //Going right
    if(j != w-1 and graph[i][j+1] and !visited[i][j+1]){
        code2 = recur(i , j+1 , count , h , w , graph, visited);
        if(code2 == 2) return 2;
    }


    if(code1 == 0 and code2 == 0) {visited[i][j] = 0; return 0;}
    else return max(code1 , code2);
}

int main() 
{
    int h , w , q;
    cin>>h>>w>>q;
    vector<vector<bool>>graph(h);
    vector<vector<bool>>visited(h);
    for(int i = 0; i<h; i++){ 
        string s;
        graph[i].resize(w);
        visited[i].resize(w);
        cin>>s;
        for(int j=0; j<w; j++){
            if(s[j] == '.')
                graph[i][j] = 1;
            else
                graph[i][j] = 0;
        }
    }
    for(int i = 0; i <q; i++){
        int k; cin>>k;
        vector<pair<int,int>>temp;
        for(int j=0; j<k; j++){
            int a,b;
            cin>>a>>b; a-=1; b-=1;
            temp.PB(make_pair(a,b));
            graph[a][b] = 0;
        }

        int code = recur(0 , 0 , 0 , h , w , graph , visited);
        if(code == 2) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        cout<<flush;
        for(int j=0; j<k; j++){
            int a = temp[j].first;
            int b = temp[j].second;
            graph[a][b] = 1;
        }
    }

    return 0; 
}