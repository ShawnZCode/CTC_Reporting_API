/****** Object:  Table [Core].[Refreshed]    Script Date: 11/17/2022 4:22:34 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [Core].[Refreshed](
	[id] [uniqueidentifier] NOT NULL,
	[refreshedAt] [datetime2](7) NOT NULL,
	[refreshedByComputerUser] [nvarchar](50) NOT NULL
	CONSTRAINT [PK_Refreshed] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
