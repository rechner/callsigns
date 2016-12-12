import unittest
import callsigns

class TestCallsigns(unittest.TestCase):
  def test_us(self):
    self.assertEqual(callsigns.get_country('ke4fox'), 'US')
    self.assertEqual(callsigns.get_country('ke4xxxx'), 'US')
    self.assertEqual(callsigns.get_country('af4r'), 'US')
    self.assertEqual(callsigns.get_country('al0xy'), 'US')
    self.assertEqual(callsigns.get_country('WA1W'), 'US')
    self.assertEqual(callsigns.get_country('N0AX'), 'US')
    self.assertEqual(callsigns.get_country('N05X'), 'US')

  def test_ca(self):
    self.assertEqual(callsigns.get_country('VA3PZR'), 'CA')
    self.assertEqual(callsigns.get_country('ve3fxy'), 'CA')
    self.assertEqual(callsigns.get_country('vo2aa'), 'CA')
    self.assertEqual(callsigns.get_country('vo2aaaa'), 'CA')

  def test_es(self):
    self.assertEqual(callsigns.get_country('AN0E'), 'ES')
    self.assertEqual(callsigns.get_country('AN39S'), 'ES')
    self.assertEqual(callsigns.get_country('eg3ffff'), 'ES')

  def test_pk(self):
    self.assertEqual(callsigns.get_country('AQ3FF'), 'PK')
    self.assertEqual(callsigns.get_country('6R3nnnn'), 'PK')

  def test_au(self):
    self.assertEqual(callsigns.get_country('ax3ff'), 'AU')
    self.assertEqual(callsigns.get_country('VK3OOO'), 'AU')
    self.assertEqual(callsigns.get_country('VZ3NNNN'), 'AU')

  def test_in(self): 
    self.assertEqual(callsigns.get_country('AU9NN'), 'IN')
    self.assertEqual(callsigns.get_country('VW3STUF'), 'IN')
    self.assertEqual(callsigns.get_country('8T9NN'), 'IN')

  def test_ar(self): 
    self.assertEqual(callsigns.get_country('AY3NNN'), 'AR')
    self.assertEqual(callsigns.get_country('AZ3N'), 'AR')
    self.assertEqual(callsigns.get_country('LP3NN'), 'AR')
    self.assertEqual(callsigns.get_country('L9A3NN'), 'AR')

  def test_uk(self):
    self.assertEqual(callsigns.get_country('2A34N'), 'UK')
    self.assertEqual(callsigns.get_country('M3XXX'), 'UK')
    self.assertEqual(callsigns.get_country('M6BGN'), 'UK')
    self.assertEqual(callsigns.get_country('2E0AAA'), 'UK')
    self.assertEqual(callsigns.get_country('2E1AGN'), 'UK')
    self.assertEqual(callsigns.get_country('2AB321N'), 'UK')
    self.assertEqual(callsigns.get_country('G6LV'), 'UK')
    self.assertEqual(callsigns.get_country('VPN3N'), 'UK')
    self.assertEqual(callsigns.get_country('VSB99A'), 'UK')
    self.assertEqual(callsigns.get_country('ZQM3A'), 'UK')
    self.assertEqual(callsigns.get_country('2BC3N'), 'UK')
    self.assertEqual(callsigns.get_country('VSX888N'), 'UK')
    self.assertEqual(callsigns.get_country('M5AAA'), 'UK')


  def test_nl(self):
    pass

  def test_unallocated(self):
    self.assertIs(callsigns.get_country('E8A1NN'), None)
    self.assertIs(callsigns.get_country('E91N'), None) 
    self.assertIs(callsigns.get_country('H51JKL'), None) 
    self.assertIs(callsigns.get_country('O31J'), None) 
    self.assertIs(callsigns.get_country('X3A3N'), None) 
    

  def test_invalid(self):
    self.assertIs(callsigns.get_country('Qui3ckbrownfox'), None)
    self.assertIs(callsigns.get_country('9AR3AQ'), None)
    self.assertIs(callsigns.get_country('WA2WWWWW'), None)
    self.assertIs(callsigns.get_country('WAAA2W'), None)
    self.assertIs(callsigns.get_country('ZQM3'), None)
    self.assertIs(callsigns.get_country('WA2N3'), None)

if __name__ == '__main__':
  unittest.main()
