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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.Text1 = wx.StaticText( self, wx.ID_ANY, u"Valorant AutoBuy", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.Text1.Wrap( -1 )

		self.Text1.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.Text1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Hotkey auswählen", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_textCtrl2.SetMaxLength( 1 )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		m_choice1Choices = [ u"STINGER", u"SPECTRE", u"BUCKY", u"JUDGE", u"BULLDOG", u"GUARDIAN", u"PHANTOM", u"VANDAL", u"MARSHAL", u"OPERATOR", u"ARES", u"ODIN" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer1.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.start_button = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.start_button, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.stop_button = wx.Button( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.stop_button, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.start_button.Bind( wx.EVT_BUTTON, self.start_buttonOnButtonClick )
		self.stop_button.Bind( wx.EVT_BUTTON, self.stop_buttonOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def start_buttonOnButtonClick( self, event ):
		event.Skip()

	def stop_buttonOnButtonClick( self, event ):
		event.Skip()


