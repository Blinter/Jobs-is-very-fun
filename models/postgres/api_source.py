"""
DB Models
Postgres
API Source Table
"""
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import TSVECTOR

from extensions_sql import db
from sqlalchemy.orm.attributes import flag_modified


class APISource(db.Model):
    """
    Unique API source used by job parser to categorize unique Jobs.
    """
    __bind_key__ = "postgres"

    __tablename__ = "api_sources"

    id = db.Column(
        db.BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.VARCHAR,
        nullable=False,
        unique=True
    )

    search_vector = db.Column(
        TSVECTOR
    )

    last_updated = db.Column(
        db.DateTime(timezone=False),
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')
    )

    listed_jobs = db.relationship(
        'ListedJob',
        back_populates="api_source",
        lazy='select',
        viewonly=True
    )

    def __repr__(self):
        """Show info about Source."""

        return ("<APISource "
                f"id={str(self.id)} "
                f"name={str(self.name)} " +

                f"last_updated={str(self.last_updated)} " +

                # (("[trunc.]" if (self.listed_jobs is not None and
                #  len(str(self.listed_jobs)) > 64) else "") +
                #  f"listed_job_job_types={str(self.listed_jobs)[:64]}"
                #  if (self.listed_jobs is not None and
                #  len(str(self.listed_jobs)) > 0) else '') +

                ">")

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_api_source_vector',
                self.search_vector,
                postgresql_using='gin'
            ),
            db.Index(
                'idx_api_source_trgm',
                self.name,
                postgresql_using='gin',
                postgresql_ops={
                    'name': 'gin_trgm_ops'
                }
            ),
        )


@db.event.listens_for(APISource, 'before_insert')
@db.event.listens_for(APISource, 'before_update')
def update_api_source_search_vector(_, __, target):
    if db.inspect(target).attrs.name.history.has_changes():
        target.search_vector = db.func.to_tsvector(target.name)
        flag_modified(target, "search_vector")
