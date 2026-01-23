def addBinary(self, a, b):
    """
     :type a: str
     :type b: str
     :rtype: str
     """
     n = int(a) + int(b)
     if n == 0:
         return "0"
      binary_str = ""
      temp_num = n
      while temp_num > 0:
          remainder = temp_num % 2
          binary_str = str(remainder) + binary_str
          temp_num //= 2
        
       return binary_str