class Solution {
    List<List<Integer>> answer = new ArrayList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        boolean[] visited = new boolean[nums.length];
        dfs(nums, visited, new ArrayList<>());

        return answer;
    }

    void dfs(int[] nums, boolean[] visited, List<Integer> current){
                if(current.size() == nums.length) {
                    answer.add(new ArrayList<>(current));
                    return;
                }

                for(int i=0;i<nums.length;i++){
                    if(visited[i]) {
                        continue;
                    }
                    visited[i] = true;
                    current.add(nums[i]);
                    dfs(nums, visited, current);
                    visited[i] = false;
                    current.remove(current.size() - 1);
                }
        }
}