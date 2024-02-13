from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
## Using SQLAlchemy2.0 generate 'items' Table Creation with association to the 'core' schema
class DB_Core_Refreshed(Base):
    __tablename__ = 'refreshed'
    __table_args__ = {"schema": "core"}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    refresheddate: Mapped[DateTime]