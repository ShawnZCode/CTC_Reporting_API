/****** Object:  Table [CMS].[Documents]    Script Date: 11/17/2022 4:22:02 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[Documents](
	[id] [uniqueidentifier] NOT NULL,
	[organizationId] [uniqueidentifier] NOT NULL,
	[fileName] [nvarchar](100) NOT NULL,
	[filePath] [nvarchar](255) NOT NULL,
	[type] [int] NOT NULL,
	[version] [int] NOT NULL,
	[revitCentralModelFilePath] [nvarchar](255) NULL,
	[revitWorkSharingMode] [int] NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Documents] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
