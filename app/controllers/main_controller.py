class Main_Controller(object):
   def __init__(self, nonce: int) -> None:
      self.nonce = nonce

   def calculate_block(self, block_len: int) -> int | float:
      return (self.nonce * 0.2) + block_len

   def retrieve_post(self, information: str) -> str:
      return information + str(self.nonce)