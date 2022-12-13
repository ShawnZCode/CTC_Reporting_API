/****** Object:  Table [CMS].[ContentFileComponents]    Script Date: 11/17/2022 4:20:17 PM ******/
SET ANSI_NULLS ON

SET QUOTED_IDENTIFIER ON

CREATE TABLE [CMS].[ContentFileComponents](
	[id] [uniqueidentifier] NOT NULL,
	[contentFileId] [uniqueidentifier] NOT NULL,
	[name] [nvarchar](150) NOT NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_ContentFileComponents] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]
