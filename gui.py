# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 732,609 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"Valorant AutoBuy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text1.Wrap( -1 )

		self.Text1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.Text1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Pick hotkey", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,30 ), wx.TE_CENTER )
		self.m_textCtrl2.SetMaxLength( 1 )
		self.m_textCtrl2.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Weapon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		m_choice1Choices = [ wx.EmptyString, u"STINGER", u"SPECTRE", u"BUCKY", u"JUDGE", u"BULLDOG", u"GUARDIAN", u"PHANTOM", u"VANDAL", u"MARSHAL", u"OPERATOR", u"ARES", u"ODIN" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer1.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Pistol", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		bSizer1.Add( self.m_staticText51, 0, wx.ALL, 5 )

		m_choice2Choices = [ wx.EmptyString, u"SHORTY", u"FRENZY", u"GHOST", u"SHERIFF" ]
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		bSizer1.Add( self.m_choice2, 0, wx.ALL|wx.EXPAND, 5 )

		m_radioBox1Choices = [ u"No Shield", u"Light Shield", u"Heavy Shield" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Shield", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer1.Add( self.m_radioBox1, 0, wx.ALL, 5 )

		m_radioBox2Choices = [ u"No Utility", u"Full Utility" ]
		self.m_radioBox2 = wx.RadioBox( self, wx.ID_ANY, u"Utility", wx.DefaultPosition, wx.DefaultSize, m_radioBox2Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox2.SetSelection( 0 )
		bSizer1.Add( self.m_radioBox2, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Add hotkey", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )


		sbSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.start_button = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.start_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.ALL, 5 )

		self.stop_button = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.stop_button, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALIGN_RIGHT|wx.ALIGN_TOP|wx.ALL|wx.LEFT, 5 )


		sbSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( sbSizer1, 0, wx.TOP|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Doubleclick to delete hotkey", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer1.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), m_listBox1Choices, 0 )
		self.m_listBox1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.m_listBox1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_textCtrl2.Bind( wx.EVT_CHAR, self.m_textCtrl2OnChar )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.m_choice1OnChoice )
		self.m_choice2.Bind( wx.EVT_CHOICE, self.m_choice2OnChoice )
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.m_radioBox1OnRadioBox )
		self.m_radioBox2.Bind( wx.EVT_RADIOBOX, self.m_radioBox2OnRadioBox )
		self.m_button5.Bind( wx.EVT_BUTTON, self.m_button5OnButtonClick )
		self.start_button.Bind( wx.EVT_BUTTON, self.start_buttonOnButtonClick )
		self.stop_button.Bind( wx.EVT_BUTTON, self.stop_buttonOnButtonClick )
		self.m_listBox1.Bind( wx.EVT_LISTBOX_DCLICK, self.m_listBox1OnListBoxDClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def m_textCtrl2OnChar( self, event ):
		event.Skip()

	def m_choice1OnChoice( self, event ):
		event.Skip()

	def m_choice2OnChoice( self, event ):
		event.Skip()

	def m_radioBox1OnRadioBox( self, event ):
		event.Skip()

	def m_radioBox2OnRadioBox( self, event ):
		event.Skip()

	def m_button5OnButtonClick( self, event ):
		event.Skip()

	def start_buttonOnButtonClick( self, event ):
		event.Skip()

	def stop_buttonOnButtonClick( self, event ):
		event.Skip()

	def m_listBox1OnListBoxDClick( self, event ):
		event.Skip()


