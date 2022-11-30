SET ANSI_NULLS ON
SET QUOTED_IDENTIFIER ON

CREATE TABLE [dbo].[Categories](
	[id] [int] NOT NULL,
	[name] [nvarchar](100) NULL,
    [fileExtension] [nvarchar](20) NULL,
	[type] [nvarchar](100) NULL,
	[refreshedId] [uniqueidentifier] NOT NULL,
	CONSTRAINT [PK_Categories] PRIMARY KEY CLUSTERED 
		([id] ASC)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF) ON [PRIMARY]
	) ON [PRIMARY]