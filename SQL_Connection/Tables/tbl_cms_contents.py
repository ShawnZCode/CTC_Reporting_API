from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey

## Using SQLAlchemy2.0 generate 'refreshed' Table Creation with association to the 'cms' schema
class Tbl_CMS_Contents(Base):
    __tablename__ = 'contents'
    __table_args__ = {"schema": "cms"}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    refresheddate: Mapped[DateTime]

## function to write to create a new entry item in the contents table
def create_new_contents_entry():
    pass

## function to read from the contents table
def get_last_from_contents():
    pass

## function to update the contents table
def update_contents_entry():
    pass

## function to delete from the contents table
def delete_contents_entry():
    pass
