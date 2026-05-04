#include <stdlib.h>

static int	lcp_len(char **strs, int size)
{
	int	i;
	int	j;

	if (!strs || size == 0 || !strs[0])
		return (0);

	i = 0;
	while (strs[0][i])
	{
		j = 1;
		while (j < size)
		{
			if (!strs[j] || strs[j][i] != strs[0][i])
				return (i);
			j++;
		}
		i++;
	}
	return (i);
}

char	*longestCommonPrefix(char **strs, int strs_size)
{
	int		i;
	int		len;
	char	*res;

	len = lcp_len(strs, strs_size);
	res = (char *)malloc(sizeof(char) * (len + 1));
	if (!res)
		return (NULL);

	i = 0;
	while (i < len)
	{
		res[i] = strs[0][i];
		i++;
	}
	res[i] = '\0';
	return (res);
}