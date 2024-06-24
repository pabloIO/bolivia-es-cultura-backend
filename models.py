from sqlalchemy import Text, String, Float, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.types import UUID
from typing import Optional, Any, List
import uuid
from datetime import datetime
from database import Base


class Users(Base):
    __tablename__ : str = "users"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"))
    username: Mapped[str] = mapped_column(String(length=50))
    email: Mapped[str] = mapped_column(String(length=50), unique=True)
    password: Mapped[str] = mapped_column(Text)
    social_media: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON)
    bio: Mapped[Optional[str]] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    role: Mapped["Roles"] = relationship(back_populates="users")
    events: Mapped[List["Events"]] = relationship(back_populates="users")

class Roles(Base):
    __tablename__ : str = "roles"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(length=50))
    description: Mapped[str] = mapped_column(String(length=100))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    permissions: Mapped[List["Permissions"]] = relationship(back_populates="roles")


class Permissions(Base):
    __tablename__ : str = "permissions"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    role_id: Mapped[UUID] = mapped_column(ForeignKey("roles.id"))
    module: Mapped[str] = mapped_column(String(length=50))
    permissions: Mapped[dict[str, Any]] = mapped_column(JSON)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    role: Mapped["Roles"] = relationship(back_populates="permissions")

class Events(Base):
    __tablename__: str = "events"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    type_event_id: Mapped[UUID] = mapped_column(ForeignKey("type_events.id"))
    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id"))
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    image: Mapped[Optional[str]] = mapped_column(Text)
    adress: Mapped[str] = mapped_column(Text)
    location: Mapped[Optional[dict[str, Any]]] = mapped_column(JSON)
    price: Mapped[float] = mapped_column(Float)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    end_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    contact_url: Mapped[Optional[str]] = mapped_column(Text)
    tiktok_url: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["Users"] = relationship(back_populates="events")


class TypeEvents(Base):
    __tablename__: str = "type_events"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    city_id: Mapped[UUID] = mapped_column(ForeignKey("cities.id"))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))   
    image: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Cities(Base):
    __tablename__: str = "cities"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(50))
    image: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
