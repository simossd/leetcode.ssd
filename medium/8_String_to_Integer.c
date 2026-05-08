int myAtoi(char* s) {
    long i;
    long num;
    long sgn;

    i = 0;
    num = 0;
    sgn = 1;
    while (s[i] && (s[i] == ' ' || s[i] == '\t'))
        i++;
    if (s[i] && (s[i] == '-' || s[i] == '+'))
    {
        if (s[i] == '-')
            sgn = -sgn;
        i++;
    }
    while (s[i] && (s[i] >= '0' && s[i] <= '9'))
    {
        num = num * 10 + (s[i] - '0');
        if (num * sgn > 2147483647)
            return (2147483647);
        if (num * sgn < -2147483648)
            return (-2147483648);
        i++;
    }
    return (num * sgn);
}