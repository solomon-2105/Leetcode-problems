class Solution {
    public int check(int[] a,int p,int k,int m) {
        int c=0,s=0;
        for(int val:a) {
            if(val<=p) {
                s++;
                if(s==k) {
                    c++;
                    if(c>=m)return c;
                    s=0;
                }
            } else {
                s=0;
            }
        }
        return c;
    }

    public int minDays(int[] a,int m,int k) {
        if(m*k>a.length)return -1;
        int mini=Integer.MAX_VALUE,maxi=Integer.MIN_VALUE;
        for(int i:a) {
            mini=Math.min(mini,i);
            maxi=Math.max(maxi,i);
        }
        int low=mini,high=maxi,ans=-1;
        while(low<=high) {
            int mid=low+(high-low)/2;
            if(check(a,mid,k,m)>=m) {
                ans=mid;
                high=mid-1;
            } else {
                low=mid+1;
            }
        }
        return ans;
    }
}
