"""
DB Models
Postgres
Listed Job Location Table
"""
from extensions_sql import db


class ListedJobLocation(db.Model):
    """
    Many-To-Many relationship that shows the described Location of a
    Listed Job.
    """
    __bind_key__ = "postgres"

    __tablename__ = "listed_job_locations"

    listed_job_id = db.Column(
        db.BigInteger,
        db.ForeignKey('listed_jobs.id'),
        primary_key=True
    )

    listed_job = db.relationship(
        'ListedJob',
        back_populates="listed_job_location",
        lazy='select',
        viewonly=True
    )

    location_id = db.Column(
        db.BigInteger,
        db.ForeignKey('locations.id'),
        primary_key=True
    )

    listed_job_location = db.relationship(
        'Location',
        back_populates="listed_job_locations",
        lazy='select',
        viewonly=True
    )

    @db.orm.declared_attr
    def __table_args__(self):
        return (
            db.Index(
                'idx_listed_job_location_listed_job_id',
                self.listed_job_id,
                postgresql_using='hash'
            ),
            db.Index(
                'idx_listed_job_location_location_id',
                self.location_id,
                postgresql_using='hash'
            ),
        )

    def __repr__(self):
        """Show info about Listed Job Location"""

        return ("<ListedJobLocation "
                
                f"listed_job={str(self.listed_job.name)} " +

                f"location={str(self.listed_job_location)} " +

                ">")
