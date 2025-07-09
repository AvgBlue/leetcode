class Solution {
    final char VISITED='#';
    private int n;
    private int m;
    private char[][] grid;
    public int numIslands(char[][] grid) {
        n=grid.length;
        m=grid[0].length;
        this.grid=grid;
        int result=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(this.grid[i][j]=='1'){
                    this.grid[i][j]=VISITED;
                    result+=1;
                    dfs(i,j);
                }
            }
            for(int k=0;k<n;k++){
                System.out.println(grid);
            }
        }
        return result;
    }
    public void dfs(int i,int j){
        int[][] directions = { {0, 1}, {1, 0},{0,-1},{-1,0} };
        for(int[] dir:directions){
            int newX=i+dir[0];
            int newY=j+dir[1];
            if(0<= newX&&newX<n && 0<=newY && newY<m &&grid[newX][newY]=='1'){
                grid[newX][newY]=VISITED;
                dfs(newX,newY);
            }
        }
    }

}