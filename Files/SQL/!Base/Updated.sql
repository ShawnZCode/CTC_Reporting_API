/****** Object:  Table [dbo].[Libraries]    Script Date: 11/17/2022 4:22:34 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Updated](
	[id] [uniqueidentifier] NOT NULL,
	[updatedAt] [datetime2](7) NOT NULL,
	[updatedByComputerUser] [nvarchar](50) NOT NULL
	CONSTRAINT [PK_Updated] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
