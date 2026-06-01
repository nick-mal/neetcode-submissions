class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or strs[0] == "":
            return ""

        prefix = strs[0]
        prefix_len = len(prefix)

        for _str in strs[1:]:
            _str_len = len(_str)

            if _str_len < prefix_len:
                prefix = prefix[:_str_len]
                prefix_len = _str_len

            if prefix != _str[:prefix_len]:
                start_search_ind = 0
                end_search_ind = prefix_len

                while start_search_ind + 1 < end_search_ind:
                    mid_search_ind = (start_search_ind + end_search_ind) // 2
                    
                    if prefix[:mid_search_ind] == _str[:mid_search_ind]:
                        start_search_ind = mid_search_ind
                    else:
                        end_search_ind = mid_search_ind
                
                if start_search_ind == 0:
                    return ""
                else:
                    prefix = _str[:start_search_ind]
        return prefix
            
                       

        