USE [master]
GO

DROP DATABASE IF EXISTS comp3920Assign1
CREATE DATABASE comp3920Assign1
GO

USE [comp3920Assign1]
/****** Object:  Table [dbo].[address]    Script Date: 2023-01-30 10:04:45 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[address](
	[address_id] [int] IDENTITY(1,1) NOT NULL,
	[house_number] [nvarchar](20) NOT NULL,
	[street_number] [nvarchar](30) NOT NULL,
	[city] [nvarchar](30) NOT NULL,
	[address_type_id] [int] NOT NULL,
 CONSTRAINT [PK_address] PRIMARY KEY CLUSTERED 
(
	[address_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[address_type]    Script Date: 2023-01-30 10:04:45 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[address_type](
	[address_type_id] [int] IDENTITY(1,1) NOT NULL,
	[type] [nvarchar](15) NOT NULL,
 CONSTRAINT [PK_address_type] PRIMARY KEY CLUSTERED 
(
	[address_type_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[address] ON 
GO
INSERT [dbo].[address] ([address_id], [house_number], [street_number], [city], [address_type_id]) VALUES (1, N'4255', N'Robson', N'Vancouver', 3)
GO
INSERT [dbo].[address] ([address_id], [house_number], [street_number], [city], [address_type_id]) VALUES (2, N'8807', N'Burrard', N'Vancouver', 2)
GO
INSERT [dbo].[address] ([address_id], [house_number], [street_number], [city], [address_type_id]) VALUES (3, N'7137', N'Maple', N'Vancouver', 2)
GO
INSERT [dbo].[address] ([address_id], [house_number], [street_number], [city], [address_type_id]) VALUES (4, N'5307', N'Lansdowne', N'Richmond', 1)
GO
SET IDENTITY_INSERT [dbo].[address] OFF
GO
SET IDENTITY_INSERT [dbo].[address_type] ON 
GO
INSERT [dbo].[address_type] ([address_type_id], [type]) VALUES (1, N'work')
GO
INSERT [dbo].[address_type] ([address_type_id], [type]) VALUES (2, N'home')
GO
INSERT [dbo].[address_type] ([address_type_id], [type]) VALUES (3, N'public')
GO
SET IDENTITY_INSERT [dbo].[address_type] OFF
GO
ALTER TABLE [dbo].[address]  WITH CHECK ADD  CONSTRAINT [FK_address_address_type] FOREIGN KEY([address_type_id])
REFERENCES [dbo].[address_type] ([address_type_id])
GO
ALTER TABLE [dbo].[address] CHECK CONSTRAINT [FK_address_address_type]
GO
