int strStr(char* haystack, char* needle) 
{
    if (strlen(haystack) < strlen(needle))
        return -1;

    int i;
    int k;
    int strstr;
    int ii;
    
    i = 0;
    while (haystack[i])
    {
        k = 0;
        strstr = i;
        ii = i;
        if (haystack[ii] == needle[k])
        {
            while (i < strlen(haystack) && k < strlen(needle) && haystack[ii] == needle[k])
            {
                ii++;
                k++;
            }
            if (needle[k] == '\0')
                return strstr;
        }
        i++;
    }
    return (-1);
}