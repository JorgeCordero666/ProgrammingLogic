# Given a string s, check if it can be constructed by taking a substring of it 
# and appending multiple copies of the substring together.

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Forma rapidda:
        # return s in (s + s)[1:-1]

        #Forma extensa:
        # Se almacena la longitud del string para saber cuantas veces se debe repetir 
        n = len(s)
        # Se recorre en un rango de 1 a n porque 0 produce
        # un sub string vacio  y no se toma en cuenta n porque
        # no es necesario repetir todo
        for i in range(1, n):
            # Si la longitud total NO se puede dividir en bloques de tamaño i, no tiene sentido probar
            if n % i != 0:
                continue

            sub_s = s[:i]
            # (n//i) es el numero de repeticiones
            sub_s = sub_s * (n // i)

            if sub_s == s:
                return True

        return False 

sol = Solution()

print(sol.repeatedSubstringPattern("aba"))