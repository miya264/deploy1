
# #SQLiteの際に使用
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from datetime import datetime


# class Base(DeclarativeBase):
#     pass


# class Customers(Base):
#     __tablename__ = 'customers'
#     customer_id: Mapped[str] = mapped_column(primary_key=True)
#     customer_name: Mapped[str] = mapped_column()
#     age: Mapped[int] = mapped_column()
#     gender: Mapped[str] = mapped_column()


# class Items(Base):
#     __tablename__ = 'items'
#     item_id: Mapped[str] = mapped_column(primary_key=True)
#     item_name: Mapped[str] = mapped_column()
#     price: Mapped[int] = mapped_column()


# class Purchases(Base):
#     __tablename__ = 'purchases'
#     purchase_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     purchase_name: Mapped[str] = mapped_column(ForeignKey("customers.customer_id"))
#     date: Mapped[datetime] = mapped_column()


# class PurchaseDetails(Base):
#     __tablename__ = 'purchase_details'
#     purchase_id: Mapped[int] = mapped_column(ForeignKey("purchases.purchase_id"), primary_key=True)
#     item_name: Mapped[str] = mapped_column(ForeignKey("items.item_id"), primary_key=True)
#     quantity: Mapped[int] = mapped_column()



#MySQLで使用
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Customers(Base):
    __tablename__ = 'customers'
    customer_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))


class Items(Base):
    __tablename__ = 'items'
    item_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    item_name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)


class Purchases(Base):
    __tablename__ = 'purchases'
    purchase_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    customer_id: Mapped[str] = mapped_column(String(10))
    purchase_date: Mapped[str] = mapped_column(String(10))


class PurchaseDetails(Base):
    __tablename__ = 'purchase_details'
    detail_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    purchase_id: Mapped[str] = mapped_column(String(10))
    item_id: Mapped[str] = mapped_column(String(10))
    quantity: Mapped[int] = mapped_column(Integer)
